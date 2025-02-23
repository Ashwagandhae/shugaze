<script lang="ts">
  export let name: string = "category";
</script>

<div class="top">
  <h2>{name}</h2>
  <div class="items">
    <slot></slot>
  </div>
</div>

<style>
  h2 {
    font-size: 2.5rem;
  }
  div.top {
    width: 100%;
  }
  .items {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
</style>
