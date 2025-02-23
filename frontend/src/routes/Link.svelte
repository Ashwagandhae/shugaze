<script lang="ts">
  export let href: string | null = null;
</script>

{#if href == null}
  <slot></slot>
{:else}
  <a {href}><slot></slot></a>
{/if}

<style>
  a {
    display: block;
    text-decoration: none;
    color: inherit;
  }
</style>
