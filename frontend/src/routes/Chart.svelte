<script lang="ts">
  import type { ShoeWithPoints } from "$lib/model";
  import { Chart, registerables } from "chart.js";
  import annotationPlugin from "chartjs-plugin-annotation";

  import { onMount } from "svelte";

  let canvasElement: HTMLCanvasElement;

  export let data: {
    originalShoe: ShoeWithPoints;
    similarShoes: ShoeWithPoints[];
    today: number;
  };

  export let similarShoesMask: boolean[];

  function shoeWithPointsToDataset(
    shoeWithPoints: ShoeWithPoints,
    special: boolean
  ) {
    let ret: any = {
      label: shoeWithPoints.shoe.name,
      data: shoeWithPoints.points.map(([x, y]) => {
        return { x, y };
      }),
      borderWidth: special ? 4 : 2,
    };
    // if (special) {
    //   ret["borderColor"] = "rgb(241, 134, 255)";
    // }
    return ret;
  }
  $: datasets = [
    shoeWithPointsToDataset(data.originalShoe, true),
    ...data.similarShoes
      .filter((_, index) => similarShoesMask[index])
      .map((s) => shoeWithPointsToDataset(s, false)),
  ];

  $: datasets, onDatasetsUpdate();

  function onDatasetsUpdate() {
    if (chart == null) return;
    chart.data.datasets = datasets;
    chart?.update();
  }

  let format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  });

  let chart: Chart;

  onMount(() => {
    Chart.register(...registerables);
    Chart.register(annotationPlugin);

    chart = new Chart(canvasElement, {
      type: "line",
      data: {
        datasets,
      },
      options: {
        plugins: {
          tooltip: {
            callbacks: {
              // Add units to the tooltip label
              label: function (item) {
                // console.log();
                return format.format(Number(item.formattedValue)); // Customize with your own unit
              },
            },
          },
          annotation: {
            annotations: {
              line1: {
                type: "line",
                xMin: data.today,
                xMax: data.today,
                borderColor: "rgb(241, 134, 255)",
                borderWidth: 2,
              },
            },
          },
        },

        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              // Set the units (e.g., "kg", "m", "s", etc.)
              callback: function (value) {
                return format.format(value as number); // Add your custom unit here
              },
            },
          },
          x: {
            type: "linear",
          },
        },
      },
    });
  });
</script>

<div class="top">
  <canvas bind:this={canvasElement}></canvas>
</div>

<style>
  .top {
    width: 100%;
  }
</style>
