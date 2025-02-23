<script lang="ts">
  import Button from "../../Button.svelte";
  import Chart from "../../Chart.svelte";
  import ShoeCard from "../../ShoeCard.svelte";

  export let data;

  export let similarShoesChecked = new Array(data.similarShoes.length).fill(
    true
  );

  $: allFalse = similarShoesChecked.every((x) => !x);
  function uncheck() {
    similarShoesChecked = new Array(data.similarShoes.length).fill(false);
  }
  function check() {
    similarShoesChecked = new Array(data.similarShoes.length).fill(true);
  }
</script>

<div class="top">
  <div class="grid">
    <div class="left">
      <ShoeCard medium shoe={data.originalShoe.shoe}></ShoeCard>
      <div class="chart">
        <Chart {data} similarShoesMask={similarShoesChecked}></Chart>
      </div>
    </div>
    <div class="right">
      <div class="similar">
        <div class="similarUpper">
          <h2>Similar shoes</h2>
          {#if allFalse}
            <Button onclick={check}>Check all</Button>
          {:else}
            <Button onclick={uncheck}>Uncheck all</Button>
          {/if}
        </div>
        <div class="similarList">
          {#each data.similarShoes as shoeWithPoints, index}
            <ShoeCard
              small
              bind:check={similarShoesChecked[index]}
              shoe={shoeWithPoints.shoe}
            ></ShoeCard>
          {/each}
          {#if data.similarShoes.length == 0}
            <p>No similar shoes found</p>
          {/if}
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .top {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 0 1rem;
    height: 100%;
  }
  .grid {
    padding-top: 1rem;
    width: 100%;
    max-width: 70rem;
    display: flex;
    gap: 1rem;
    flex-direction: row;
    height: 100%;
    box-sizing: border-box;
  }
  .left {
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 1rem;
    box-sizing: border-box;
  }
  .right {
    display: flex;
    flex-direction: row;
    height: 100%;
    box-sizing: border-box;
  }
  .similarUpper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    align-items: center;
  }
  .similar {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    width: 20rem;
    box-sizing: border-box;
  }
  .similarList {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    width: 100%;
    box-sizing: border-box;
  }
  div.chart {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0px 0px 20px rgba(61, 61, 61, 0.2);
    border-radius: 1rem;
    box-sizing: border-box;
    padding: 1rem;
  }
  div.similar {
    box-shadow: 0px 0px 20px rgba(61, 61, 61, 0.2);
    padding: 1rem;
    border-radius: 1rem;
    height: 100%;
  }

  h2 {
    margin: 0;
  }
</style>
