import axios from "../ApiHelper";


export let API = {
    getBlsLabel: () => axios.get("/api/bls_label"),
    getEurostatLabel: () => axios.get("/api/eurostat_label"),
    getFeatureRanges: () => axios.get("/api/feature_ranges"),
    retrieveTimeSeries: (data) =>  axios.post("/api/macro_data", data),
}