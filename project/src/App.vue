<template>
  <BsLayoutDefault docTitle="Solution Name" :docIcon="docLogo">
    <template #header>
      <div class="dku-medium-title-sb q-pa-md">Header</div>
    </template>
    <template #leftpanel>
      <div class="dku-medium-title-sb q-pa-md">Selectors</div>
      <BsSelect 
            v-model="geo_model" 
            :options="geo_options" 
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
            :options="series_options" 
            clearable 
            multiple 
            use-chips 
            bsLabel="Series"
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
    </template>
  </BsLayoutDefault>
</template>
<script>
  import docLogo from "./assets/images/doc-logo-example.svg"
  import { API } from "./Api";
  export default {
    data() {
      return {
        docLogo,
        hello: "",
        geo_model: [],
        geo_options: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        geo_allOptions: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        series_model: [],
        series_options: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        series_allOptions: ['Dataiku','Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'],
        date_model: { from: '2020/07/08', to: '2020/07/17' },
        type_model: true,
      }
    },
    mounted: function() {
      API.getHello().then(response => {
        this.hello = response;
        console.log(response)
      }).catch((err) => {
        console.log(err);
      })
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
          filterFn: function(val, update, abort) {
              update(() => {
              const needle = val.toLowerCase()
              this.options = this.allOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
              })
          }
      }
  }
</script>