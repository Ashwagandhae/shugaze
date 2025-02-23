<script lang="ts">
  import { similar } from "$lib/request";
  import Category from "../../Category.svelte";
  import Search from "../../Search.svelte";
  import ShoeCard from "../../ShoeCard.svelte";

  export let data;
</script>

<div class="top">
  <div class="categories">
    <Search initSearch={data.search}></Search>
    <Category name={`Search results for "${data.search}"`}>
      {#each data.results as shoe}
        <ShoeCard {shoe}></ShoeCard>
      {/each}
    </Category>
    <!-- <Category name="Cheap"></Category> -->
  </div>
</div>

<style>
  .top {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .categories {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    width: 100%;
    max-width: 50rem;
  }
</style>
