<template>
  <div>
    <ClientHeader />
    <ClientGlobalMenu />
    <h1>全国査定</h1>

    全国査定
  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientGlobalMenu from '@/components/client/ClientGlobalMenu.vue'
  // import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
      }
    },
    components: {
      ClientHeader,
      ClientGlobalMenu,
    },
    methods: {
    },
    mounted(){

    },
  }
</script>

<style>

</style>