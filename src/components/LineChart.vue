<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      gradient: null,
      gradient2: null,
      gradient3: null
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
    this.gradient3 = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.gradient.addColorStop(0, "rgba(140, 82, 255, 0.5)");
    this.gradient.addColorStop(0.5, "rgba(140, 82, 255, 0.25)");
    this.gradient.addColorStop(1, "rgba(140, 82, 255, 0)");

    this.gradient2.addColorStop(0, "rgba(28, 56, 251, 0.9)");
    this.gradient2.addColorStop(0.5, "rgba(25, 56, 251, 0.25)");
    this.gradient2.addColorStop(1, "rgba(25, 56, 251, 0)");

    this.gradient3.addColorStop(0, "rgba(150, 150, 150, 0.9)");
    this.gradient3.addColorStop(0.5, "rgba(160, 160, 160, 0.25)");
    this.gradient3.addColorStop(1, "rgba(150, 150, 150, 0)");

    this.chartdata.datasets[0].backgroundColor = this.gradient;
    if (this.chartdata.datasets.length == 2)
    this.chartdata.datasets[1].backgroundColor = this.gradient2;

    if (this.chartdata.datasets.length == 3)
    this.chartdata.datasets[2].backgroundColor = this.gradient3;


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