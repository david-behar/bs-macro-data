<template>
  <div class="chart_area">
    <div class="chart_container chart_panel">
      <div class="chart_data">
        <v-chart
          class="chart"
          :option="option"
          style="height: 100% display: flex;"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import {
  PieChart,
  LineChart,
  ScatterChart,
  GaugeChart,
  SankeyChart,
  HeatmapChart,
  BarChart,
} from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  VisualMapComponent,
  DataZoomComponent,
} from "echarts/components";
import VChart from "vue-echarts";
import { API } from "../Api";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  LineChart,
  ScatterChart,
  GaugeChart,
  SankeyChart,
  VisualMapComponent,
  HeatmapChart,
  BarChart,
  DataZoomComponent,
]);

export default {
  name: "BsEchart",
  props: ["option"],

  updated: function () {
    if (!this.option) {
      console.log("option not initialized");
    }
  },
  components: {
    VChart,
  },
};
</script>

<style scoped>
.chart_area {
  min-height: 1px;
  float: left;
  margin: 10px;
  height: 500px;
  width: 500px;
}

.chart_container {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  align-items: center;
}

.chart_panel {
  width: 100%;
  height: 100%;
  display: inline-block;
  background: #fff;
  border: 1px solid #e6e9ed;
  border-radius: 10px;
  -webkit-column-break-inside: avoid;
  -moz-column-break-inside: avoid;
  column-break-inside: avoid;
  opacity: 1;
  -moz-transition: all 0.2s ease;
  -o-transition: all 0.2s ease;
  -webkit-transition: all 0.2s ease;
  -ms-transition: all 0.2s ease;
  transition: all 0.2s ease;
}

.chart_container .chart_data {
  height: 100%;
  width: 100%;
}
</style>