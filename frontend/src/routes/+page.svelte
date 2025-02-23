<script lang="ts">
  import { similar } from "$lib/request";
  import BigLogo from "./BigLogo.svelte";
  import Category from "./Category.svelte";
  import Search from "./Search.svelte";
  import ShoeCard from "./ShoeCard.svelte";

  export let data;
</script>

<!-- <button onclick={ohio}>test</button>
<h1>Welcome to SvelteKit</h1>
<p>
  Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the
  documentation
</p> -->

<div class="top">
  <div class="categories">
    <BigLogo></BigLogo>
    <Search></Search>
    <Category name="Trending">
      {#each data.trendingShoes as shoe}
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
