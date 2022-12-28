from flask import Blueprint, jsonify


fetch_api = Blueprint("fetch_api",__name__)

@fetch_api.route("/api/feature_ranges")
def get_feature_ranges():
    feature_ranges_dataset = project.get_dataset("feature_ranges")
    feature_ranges = []
    for i, row in enumerate(feature_ranges_dataset.iter_rows()):
        feature_range = {'variable': row[0]}
        feature_range['values'] = row[4].replace('[', '').replace(']', '').replace("'", "").split(', ')
        feature_range['id'] = i
        feature_ranges.append(feature_range)
    return jsonify(feature_ranges)

@fetch_api.route("/api/bls_label")
def get_feature_ranges():
    bls_label_dataset = project.get_dataset("bls_label")
    bls_labels = []
    for i, row in enumerate(bls_label_dataset.iter_rows()):
        bls_label = {'series_id': row[0], 'name': row[1], 'id': i}
        bls_labels.append(bls_label)
    return jsonify(bls_labels)

@fetch_api.route("/api/eurostat_label")
def get_feature_ranges():
    eurostat_label_dataset = project.get_dataset("eurostat_label")
    eurostat_labels = []
    for i, row in enumerate(eurostat_label_dataset.iter_rows()):
        eurostat_label = {'series_id': row[0], 'name': row[1], 'id': i}
        eurostat_labels.append(eurostat_label)
    return jsonify(eurostat_labels)

@fetch_api.route("/api/macro_data")
def retrieve_macro_data(params):
    client = dataikuapi.APINodeClient("http://a39c8ea18d8cb4364aa8efb6814193fc-1014597043.eu-west-3.elb.amazonaws.com:12000", "macro_data")
    result = client.run_function("macro_lookup",
            geo = ["USA"],
            start_date = "2016-01-01",
            end_date = "2017-01-01",
            series_type = "eurostat",
            series_id = ["C1105"])
    return result.get("response")