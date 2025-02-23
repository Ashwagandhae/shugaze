<script lang="ts">
  import Link from "./Link.svelte";

  export let color: "green" | "blue" = "green";
  export let href: string | null = null;
  export let small: boolean = false;
  export let onclick: (event: MouseEvent) => void = () => {};
</script>

<Link {href}>
  <button
    {onclick}
    class:small
    class:green={color == "green"}
    class:blue={color == "blue"}
  >
    <slot></slot>
  </button>
</Link>

<style>
  button {
    display: flex;
    flex-direction: row;
    gap: 0.5rem;

    border: none;
    box-sizing: border-box;
    border-radius: 1.2rem;
    margin: 0;
    font-size: 1.1rem;

    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0.5rem;

    width: min-content;
    white-space: nowrap;
    background: rgb(var(--back));

    transition:
      transform 0.3s,
      box-shadow 0.3s;
  }
  .green {
    --back: 113, 255, 172;
  }
  .blue {
    --back: 241, 134, 255;
  }
  button.small {
    font-size: 0.9rem;
    padding: 0.5rem;
  }

  button:hover {
    box-shadow: 0px 0px 20px rgba(var(--back), 0.8);
    transform: scale(1.05);
  }
  button:active {
    transform: scale(0.95);
  }
</style>
