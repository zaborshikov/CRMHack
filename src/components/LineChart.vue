<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      gradient: null,
      gradient2: null
    };
  },
  props: ['chartdata'],
  mounted() {
    this.gradient = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.gradient2 = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.gradient.addColorStop(0, "rgba(140, 82, 255, 0.5)");
    this.gradient.addColorStop(0.5, "rgba(140, 82, 255, 0.25)");
    this.gradient.addColorStop(1, "rgba(140, 82, 255, 0)");

    this.gradient2.addColorStop(0, "rgba(25, 241, 235, 0.9)");
    this.gradient2.addColorStop(0.5, "rgba(25, 241, 235, 0.25)");
    this.gradient2.addColorStop(1, "rgba(25, 241, 235, 0)");

    this.chartdata.datasets[0].backgroundColor = this.gradient;
    this.chartdata.datasets[1].backgroundColor = this.gradient2;

    this.renderChart(
      this.chartdata,
      { responsive: true, maintainAspectRatio: false }
    );
    
  }
};
</script>
<style>
canvas#line-chart {
  height: 60vh!important;
}
</style>