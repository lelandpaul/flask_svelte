<style>
  div {
    font-size: 2rem;
  }
</style>

<script>
	import Folder from './Folder.svelte';

  let root = window.root;

</script>


<Folder name="Flask Project" files={root} expanded/>
