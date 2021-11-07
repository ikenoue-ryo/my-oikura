<template>
  <div>
    <TopNavi />
  <v-container class="pa-8">
    <v-row class="mt-5">
      <v-col>
        <div v-if="assesments">
          {{assesments.length}}件 の査定金額を表示します
          <template>
            <div
              class="mt-3 row"
              tile
            >
              <v-list flat width="100%">
                <v-list-item-group
                  color="black"
                >
                  <v-list-item
                    v-for="(assesment, i) in assesments"
                    :key="i"
                    class="pa-0"
                    :href="`/offer-form/${assesment.id}/`"
                  >
                    <v-list-item-icon>
                      <v-img :src="assesment.offer.image" width="100" height="auto" :class="`rounded-lg`"></v-img>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>{{assesment.offer.item_name}} {{assesment.offer.grade}}</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-content class="assesment">
                      <div class="font-weight-bold">{{assesment.value | priceLocaleString }} 円</div>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </div>
          </template>
        </div>
      </v-col>
    </v-row>
  </v-container>
  
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
        assesments: [],
      }
    },
    components: {
      TopNavi,
      BottomNavi,
    },
    filters: {
      priceLocaleString: function (value) {
          return value.toLocaleString()
      }
    },
    mounted(){
      api({
        method: 'get',
        url: '/assesment_price/',
      })
      .then(response => this.assesments = response.data.results.filter(assesment => assesment.offer.category.name ==  this.$route.params['carname']))
      .catch(error => console.log(error)); 
    },
  }
</script>

<style scoped>
  .assesment {
    position: absolute;
    right: 10px;
    bottom: 45px;
  }
</style>