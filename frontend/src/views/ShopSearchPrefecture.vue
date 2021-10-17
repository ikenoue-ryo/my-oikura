<template>
  <div>
    <Header />
    <GlobalMenu />
    <br>
    <h2>{{shop_Info[0].prefectures}}の検索結果を表示中</h2>

    <div v-for="shop in shop_Info" :key="shop.id">
      <router-link :to="`/client/shop/${shop.id}`">
        <ul>
          <li><img :src="shop.img" alt="" width=200></li>
          <li>{{shop.name}}</li>
          <li>{{shop.manager}}</li>
          <li>{{shop.tel}}</li>
          <li>{{shop.place}}</li>
        </ul>
      </router-link>
      <hr>
    </div>


  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import api from '@/services/api'

  export default {
    name: 'Mypage',
    data() {
      return {
        shop_Info: [],
      }
    },
    components: {
      Header,
      GlobalMenu,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/api/client',
      })
      .then(response => this.shop_Info = response.data.results.filter(prefecture => prefecture.assesment_price.client_shop.prefectures === this.$route.params['prefecture']))
      .catch(error => console.log(error))
    },
    computed: {

    }
  }
</script>

<style>
/* this.$route.params['prefecture'] */
</style>