<template>
  <BsLayoutDefault docTitle="Solution Name" :docIcon="docLogo">
    <template #header>
      <div class="dku-medium-title-sb q-pa-md">Production Price Indices</div>
    </template>
    <template #leftpanel>
      <div class="dku-medium-title-sb q-pa-md">Selectors</div>
      <BsSelect 
            v-model="geo_model" 
            :options="getGeoOptions()" 
            clearable 
            multiple 
            use-chips 
            bsLabel="Geography"
            clear-icon="clear" 
            @filter="filterFn"
            use-input
            input-debounce="0">
            <template v-slot:selected-item="scope">
                <q-chip
                    removable
                    square
                    @remove="scope.removeAtIndex(scope.index)"
                    :tabindex="scope.tabindex"
                    class="q-mr-xs bs-chip__select"
                    icon-remove="clear"
                    text-color="white">
                    {{ scope.opt }}
                </q-chip>
            </template>
        </BsSelect>
        <BsDateRange v-model="date_model" bsLabel="Date"></BsDateRange>
        <BsToggle v-model="type_model" labelRight="Eurostat" labelLeft="BLS"/>
        <BsSelect 
            v-model="series_model" 
            :options="getSeriesOptions()" 
            clearable 
            multiple 
            use-chips 
            bsLabel="Series"
            clear-icon="clear" 
            @filter="filterFnSeries"
            use-input
            input-debounce="0">
            <template v-slot:selected-item="scope">
                <q-chip
                    removable
                    square
                    @remove="scope.removeAtIndex(scope.index)"
                    :tabindex="scope.tabindex"
                    class="q-mr-xs bs-chip__select"
                    icon-remove="clear"
                    text-color="white">
                    {{ scope.opt }}
                </q-chip>
            </template>
        </BsSelect>
        <BsButton class="bs-btn dku-text" unelevated @click="retrieveData">Retrieve</BsButton>
    </template>
    <template #documentation>
      <p class="dku-small-title">Description 1</p>
      <p class="dku-text">Use filters to discover your process through the data. 
              Remove noisy activities through the bottom filters. 
              Processes displayed in the main screen can be saved as reference and 
              compared through conformance checks and individual traces.</p>
      <p class="dku-small-title">Description 2</p>
      <p class="dku-text">Use filters to discover your process through the data. 
              Remove noisy activities through the bottom filters. 
              Processes displayed in the main screen can be saved as reference and 
              compared through conformance checks and individual traces.</p>
      <p class="dku-small-title">Description 3</p>
      <p class="dku-text">Use filters to discover your process through the data. 
              Remove noisy activities through the bottom filters. 
              Processes displayed in the main screen can be saved as reference and 
              compared through conformance checks and individual traces.</p>
      <p class="dku-small-title">Description 4</p>
      <p class="dku-text">Use filters to discover your process through the data. 
              Remove noisy activities through the bottom filters. 
              Processes displayed in the main screen can be saved as reference and 
              compared through conformance checks and individual traces.</p>
      
    </template>
    <template #content>
      <BsEcharts/>
    </template>
  </BsLayoutDefault>
</template>
<script>
  import docLogo from "./assets/images/doc-logo-example.svg"
  import { API } from "./Api";
  import BsEcharts from "./components/BsEcharts.vue";
  export default {
    components: {
      BsEcharts,
    },
    data() {
      return {
        docLogo,
        hello: "",
        geo_model: [],
        geo_options: [],
        geo_allOptions: [],
        series_model: [],
        series_options: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        series_allOptions: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        eurostat_options: [],
        bls_options: [],
        date_model: { from: '2020/07/08', to: '2020/07/17' },
        type_model: true,
        feature_ranges: {},
      }
    },
    created() {
          API.getBlsLabel().then(response => {
              this.bls_label = response;
          })
          API.getEurostatLabel().then(response => {
              this.eurostat_label = response;
          })
          API.getFeatureRanges().then(response => {
              this.feature_ranges = response;
          })
      },
    methods: {
          getGeoOptions: function() {
            for (let i = 0; i<this.feature_ranges.length; i++) {
                let variable = this.feature_ranges[i];
                if (variable['variable'] == 'geo') {
                  this.geo_options = variable['values'];
                  this.geo_allOptions = variable['values'];
                } else if (variable['variable'] == 'NACE Rev. 2') {
                  this.eurostat_options = variable['values'];
                } else if (variable['variable'] == 'US NAICS 2017') {
                  this.bls_options = variable['values'];
                } else if (variable['variable'] == 'date') {
                  this.date_model['from'] = variable['values'][0];
                  this.date_model['to'] = variable['values'][1];
                }
              }
            return this.geo_options;
          },
          getSeriesOptions: function() {
            let options = [];
            if (this.type_model) {
              options = this.eurostat_options;
              this.series_allOptions = [...this.eurostat_options];
            } else {
              options = this.bls_options;
              this.series_allOptions = [...this.bls_options];
            }
            return options;
          },
          filterFn: function(val, update, abort) {
              update(() => {
              const needle = val.toLowerCase()
              this.geo_options = this.geo_allOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
              })
          },

          filterFnSeries: function(val, update, abort) {
              update(() => {
              const needle = val.toLowerCase()
              this.series_options = this.series_allOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
              })
          },

          retrieveData: function() {
              let params = {};
              let res = 0;
              API.retrieveTimeSeries(params).then(response => {
                res = response;
              });
              //console.log(data);
          }
      }
  }
</script>