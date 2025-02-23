<script lang="ts">
  import logoImage from "$lib/assets/logo.png";
</script>

<div class="top">
  <div class="logo" style={`--image: url("${logoImage}")`}></div>
  <h2>ShuGaze</h2>
  <div class="logo rev" style={`--image: url("${logoImage}")`}></div>
</div>

<style>
  .top {
    padding-top: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow-x: hidden;
    width: 100vw;
  }

  h2 {
    margin: 0;
    font-size: 7rem;
    animation: scaleIn 3s ease;
  }
  @keyframes scaleIn {
    from {
      scale: 0;
    }
    to {
      scale: 1;
    }
  }

  .logo {
    background: var(--image);
    /* background-size: 400px 100px; */
    background-repeat: repeat-x;
    width: 120rem;
    background-size: 20rem 20rem;
    height: 20rem;
    animation: scrollBackground 5s linear infinite;
  }

  @keyframes scrollBackground {
    from {
      transform: translateX(0);
    }
    to {
      transform: translateX(-20rem);
    }
  }
  @keyframes scrollBackgroundRev {
    from {
      transform: translateX(0);
    }
    to {
      transform: translateX(20rem);
    }
  }
  .logo.rev {
    animation: scrollBackgroundRev 5s linear infinite;
  }
</style>
