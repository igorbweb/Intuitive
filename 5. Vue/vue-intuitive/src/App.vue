<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100">
    <OperadoraSearch />
  </div>
</template>

<script>
import OperadoraSearch from "./components/BuscarOperadora.vue";

export default {
  components: { OperadoraSearch },
};
</script>