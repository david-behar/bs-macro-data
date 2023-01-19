from flask import Blueprint, request, jsonify
from .python import graphs_utils as gu
import dataiku
import pandas as pd
import numpy as np
import json
import dataikuapi
from commons.python.fetch.config_bs import ConfigBs, EnvMode

mode = ConfigBs.mode()

fetch_api = Blueprint("fetch_api",__name__)
client = dataiku.api_client()
if mode == EnvMode.LOCAL.value:
    project_key = "SOL_MACRO_API"
else:
    project_key = dataiku.get_custom_variables()["projectKey"]
project = client.get_project(project_key)

fetch_api = Blueprint("fetch_api",__name__)

def to_json(o):
    # np.int64 do not inherit from int so it needs a special handling
    if isinstance(o, np.int64):
        return int(o)
    return o.__dict__

@fetch_api.route("/api/feature_ranges")
def get_feature_ranges():
    feature_ranges_dataset = project.get_dataset("feature_ranges")
    feature_ranges = []
    for i, row in enumerate(feature_ranges_dataset.iter_rows()):
        feature_range = {'variable': row[0]}
        feature_range['values'] = row[1].replace('[', '').replace(']', '').replace("'", "").split(', ')
        feature_range['id'] = i
        feature_ranges.append(feature_range)
    return jsonify(feature_ranges)

@fetch_api.route("/api/bls_label")
def get_bls_label():
    bls_label_dataset = project.get_dataset("bls_label")
    bls_labels = []
    for i, row in enumerate(bls_label_dataset.iter_rows()):
        bls_label = {'series_id': row[0], 'name': row[1], 'id': i}
        bls_labels.append(bls_label)
    return jsonify(bls_labels)

@fetch_api.route("/api/eurostat_label")
def get_eurostat_label():
    eurostat_label_dataset = project.get_dataset("eurostat_label")
    eurostat_labels = []
    for i, row in enumerate(eurostat_label_dataset.iter_rows()):
        eurostat_label = {'series_id': row[0], 'name': row[1], 'id': i}
        eurostat_labels.append(eurostat_label)
    return jsonify(eurostat_labels)

@fetch_api.route("/api/macro_data", methods=["POST"])
def retrieve_macro_data():
    data = request.get_json()
    print('retrieve')
    client = dataikuapi.APINodeClient("http://a39c8ea18d8cb4364aa8efb6814193fc-1014597043.eu-west-3.elb.amazonaws.com:12000", "macro_data")
    result = client.run_function("macro_lookup",
            geo = ["USA"],
            start_date = "2016-01-01",
            end_date = "2017-01-01",
            series_type = "eurostat",
            series_id = ["C1105"])
    data = pd.read_json(result.get("response"))
    print('done')
    print(len(data))
    print(data)
    print(data["date"])
    #line_series = gu.generateLineSeries(data[["date", "value", "NACE Rev. 2"]], "date", "value", "NACE Rev. 2", nb_bin=50)
    line_series = gu.LineSeries(list(zip(data["date"], data["value"])), legend_name="value")
    line_series.color = data["NACE Rev. 2"]
    chart = gu.XYChart('date', 'value', 'value', line_series, graph_subtitle='PPI over time', dataZoom=True)
    print(json.dumps({"line_series" : line_series}, default=to_json))
    print(chart)
    print(to_json(chart))
    #chart.option["color"] = shades_of_blue

    return json.dumps({"chart" : chart}, default=to_json)