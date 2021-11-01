<template>
  <div>
    <TopNavi />
    <br>
    <br>
    <br>

    <v-container>
      <v-col>
        <v-row>
          <v-col
            v-for="(car, i) in cars"
            :key="i"
            cols="4"
            v-ripple
            class="rounded-lg pa-2"
          >
          <a :href="`/list-cars/${car.name}`">
            <!-- <v-subheader>{{car.brand.name}}</v-subheader> -->
            <img
              :src="car.image"
              class="image rounded-lg"
              height="auto"
              width="100%"
            >
            {{car.name}}
            </a>
          </v-col>
        </v-row>
      </v-col>
    </v-container>
  
    <div class="push"></div>
    <BottomNavi />
  </div>
</template>

<script>
  import TopNavi from '@/components/TopNavi.vue'
  import BottomNavi from '@/components/BottomNavi.vue'
  import api from '@/services/api'

  export default {
    name: 'ListCars',
    data() {
      return {
        cars: [],
        brands: [],
      }
    },
    components: {
      TopNavi,
      BottomNavi,
    },
    methods: {
    },
    mounted(){
      api({
        method: 'get',
        url: '/car/',
      })
      .then(response => this.cars = response.data.results)
      .catch(error => console.log(error));

      api({
        method: 'get',
        url: '/brand/',
      })
      .then(response => this.brands = response.data.results)
      .catch(error => console.log(error)); 
    },
  }
</script>

<style scoped>
  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }
</style>