<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Registration from './pages/Registration.svelte';

  let pageType = 'registration';
</script>

<main>
  {#if pageType === 'registration'}
    <Registration />
  {:else}
    <Counter />
  {/if}
</main>

<style>
  .theme{
    @apply text-2xl;
  }
</style>
