<template>
  <div>
    <Header />
    <GlobalMenu />
    <br>

    <v-container>
    <template>
      <v-card>
        <v-tabs
          color="deep-purple accent-4"
          right
        >
          <v-tab>TOYOTA</v-tab>
          <v-tab>HONDA</v-tab>
          <v-tab>MAZDA</v-tab>
          <v-tab>SUZUKI</v-tab>
          <v-tab>DAIHATSU</v-tab>

          <v-tab-item
            v-for="n in 5"
            :key="n"
          >
            <v-container fluid>
              <v-row>
                <v-col
                  v-for="car_info in car"
                  :key="car_info"
                  cols="12"
                  md="3"
                >
                  <v-img
                    :src="`${car_info.image}`"
                    max-height="150"
                    max-width="250"
                    aspect-ratio="1"
                  ></v-img>
                  {{car_info.name}}
                </v-col>
              </v-row>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </template>
    </v-container>


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
        car: []
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
        url: '/api/v1/api/car/',
      })
      .then(response => this.car = response.data.results)
      .catch(error => console.log(error));
    },
    computed: {

    }
  }
</script>

<style>

</style>