<template>
  <div>
    <Header />
    <GlobalMenu />
    <v-container>
      <h1>店舗ページ</h1>

      <h2>店舗情報</h2>
      <p>ID: {{ shop_infos.id }}</p>
      <p>店舗名: {{ shop_infos.name }}</p>
      <p>店舗名カナ: {{ shop_infos.kana }}</p>
      <p>店舗画像 <img :src="shop_infos.img" alt="" width=200></p>
      <p>担当者: {{ shop_infos.manager }}</p>
      <p>電話番号: {{ shop_infos.tel }}</p>
      <p>Email: {{ shop_infos.email }}</p>
      <p>所在地: {{ shop_infos.place }}</p>
      <p>作成日: {{ shop_infos.created_on }}</p>
      <p>営業時間</p>
      <p>買取方法</p>
      <hr>
      <br><br><br>
      <div v-for="review in shop_Review" :key="review.id">
        <ul>
          <li>{{review.author.name}}</li>
          <li>{{review.comment}}</li>
          <li>
            <v-rating
              v-model="review.score"
              background-color="orange lighten-3"
              color="orange"
              size="50"
            ></v-rating>
          </li>
          <li>{{review.created_at}}</li>
        </ul>
      </div>
      <VisitReservation />

      <h3>店舗ブログ</h3>
      <div v-for="shop in shop_Pr" :key="shop.id">
        <p><v-img :src="shop.img" width="500px"></v-img></p>
        <p>{{shop.text}}</p>
        <p>{{shop.created_at}}</p>
      </div>
    </v-container>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue'
  import GlobalMenu from '@/components/GlobalMenu.vue'
  import VisitReservation from '@/components/VisitReservation.vue'
  import api from '@/services/api'

  export default {
    name: 'Home',
    data() {
      return {
        mypage: '',
        client: '',
        rating: '',
        shop_Info: [],
        profiles: [],
        shop_Review: [],
        shop_Pr: [],
      }
    },
    components: {
      Header,
      GlobalMenu,
      VisitReservation,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/api/v1/auth/users/me/',
      })
      .then(response => this.mypage = response.data)
      .catch(error => console.log(error));
      
      api({
        method: 'get',
        url: '/api/v1/api/client/' + this.$route.params['id']
      })
      .then(response => this.shop_Info = response.data)
      .catch(error => console.log(error))

      api({
        method: 'get',
        url: '/api/v1/api/shop_review/'
      })
      .then(response => this.shop_Review = response.data.results.filter(review => review.client_shop == this.$route.params['id']))
      .catch(error => console.log(error))

      api({
        method: 'get',
        url: '/api/v1/api/client_pr/'
      })
      .then(response => this.shop_Pr = response.data.results.filter(shop => shop.client_shop == this.$route.params['id']))
      .catch(error => console.log(error))
    },
    computed: {
      email() {
        return this.$store.getters['auth/email']
      },
      // user_profile() {
      //   const profiles = this.profiles.results.find(profiles => profiles.user.email === this.email)
      //   return profiles;
      // }
      shop_infos() {
        const shop_info = this.shop_Info;
        return shop_info;
      }
    }
  }
</script>

<style>

</style>