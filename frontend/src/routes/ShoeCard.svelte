<script lang="ts">
  import shoeImage from "$lib/assets/image.png";
  import { shoeImages } from "$lib/image";
  import type { Shoe } from "$lib/model";
  import Button from "./Button.svelte";
  import Analytics from "~icons/mdi/Analytics";
  import ShoppingCart from "~icons/mdi/ShoppingCart";

  export let shoe: Shoe;
  export let small: boolean = false;
  export let medium: boolean = false;
  export let check: boolean | null = null;

  let image = (shoeImages as any)[shoe.name] ?? shoeImages["New Balance 2002R"];
  function buy() {
    console.log("gyatt");
    window.open("https://stockx.com/search?s=" + shoe.name, "_blank");
  }

  let format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  });
  $: formattedPrice = format.format(shoe.price);
</script>

<div class="card" class:small class:medium>
  <div class="description">
    <div class="upper">
      {#if check !== null}
        <input type="checkbox" bind:checked={check} />
      {/if}
      <h3>{shoe.name}</h3>
      {#if !small && !medium}
        <div class="price">{formattedPrice}</div>
      {/if}
    </div>
    <div class="lower">
      {#if !small && !medium}
        <p>
          Size: {shoe.size}
        </p>
        <div class="buttons">
          <Button href={"/analyze/" + shoe.id}
            >Analyze shoe <Analytics /></Button
          >
          <Button color="blue" onclick={buy}>Buy now <ShoppingCart /></Button>
        </div>
      {:else}
        <div class="buttons">
          <Button color="blue" {small} onclick={buy}>
            {formattedPrice}
            <ShoppingCart />
          </Button>
          {#if medium}
            <p>
              Size: {shoe.size}
            </p>
          {/if}
          {#if !medium}
            <Button {small} href={"/analyze/" + shoe.id}
              >Analyze <Analytics /></Button
            >
          {/if}
        </div>
      {/if}
    </div>
  </div>
  <div class="image">
    <img alt="shoe" src={image} />
  </div>
</div>

<style>
  .card {
    width: 100%;
    height: min-content;
    display: flex;
    flex-direction: row;
    box-shadow: 0px 0px 30px rgba(61, 61, 61, 0.2);
    box-sizing: border-box;
    border-radius: 1rem;
    justify-content: space-between;
  }

  .small {
    box-shadow: 0px 0px 10px rgba(61, 61, 61, 0.1);
  }

  img {
    object-fit: cover;
    /* border-radius: 50%; */
    /* height: 15rem; */
    width: 15rem;
  }

  .medium img {
    /* width: 6rem; */
    height: 6rem;
  }

  .small img {
    /* height: 5rem; */
    width: 4rem;
    /* height: 2.5; */
  }
  .image {
    padding: 1rem;
  }

  .small .image {
    padding: 0.5rem;
  }
  .description {
    display: flex;
    flex-direction: column;
    padding: 1rem 0rem 1rem 1rem;
    justify-content: space-between;
    width: 100%;
  }
  .small .description {
    width: calc(100% - 5rem - 2rem);
  }

  .upper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }

  h3 {
    margin: 0;
    font-size: 2rem;
  }

  .small h3 {
    font-size: 1.1rem;
    white-space: nowrap; /* Prevent text wrapping */
    overflow: hidden; /* Hide overflowed content */
    text-overflow: ellipsis;
    width: 100%;
  }

  .lower p {
    font-size: 1rem;
    line-height: 1.6;
  }
  .lower {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
  }
  .small .lower,
  .medium .lower {
    height: auto;
  }
  .price {
    padding: 0.5rem;
    background: rgb(240, 240, 240);
    border-radius: 0.5rem;
    font-size: 1.5rem;
  }

  .small .price {
    font-size: 0.9rem;
  }

  .buttons {
    display: flex;
    flex-direction: row;
    gap: 0.5rem;
    align-items: center;
  }
</style>
