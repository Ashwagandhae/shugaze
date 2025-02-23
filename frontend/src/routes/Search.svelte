<script lang="ts">
  import Button from "./Button.svelte";
  import { goto } from "$app/navigation";

  export let initSearch: string = "";

  let search = initSearch;

  function handleKeyDown(e: KeyboardEvent) {
    if (e.key == "Enter") {
      doSearch();
    }
  }

  function doSearch() {
    if (search.length == 0) return;
    goto("/search/" + search);
  }
</script>

<div class="search">
  <input
    type="text"
    placeholder="Search for shoes..."
    bind:value={search}
    onkeydown={handleKeyDown}
  />
  <Button onclick={doSearch}>search</Button>
</div>

<style>
  .search {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin-top: 3rem;
    gap: 1rem;
    border-radius: 1rem;
    box-shadow: 0px 0px 30px rgba(61, 61, 61, 0.2);
    box-sizing: border-box;
    padding-right: 1rem;
  }
  .search input {
    width: 100%;
    background: none;
    border: none;
    font-size: 1.1rem;
    padding: 1.5rem;
    border-radius: 1.2rem;
  }
</style>
