<template>
  <div>
    <TopNavi />
  <v-container class="pa-8">
    <v-row class="mt-5">
      <v-col>
        <div v-if="clients">
          査定金額に評判の良い店舗を表示しています。
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
                    v-for="(client, i) in clients"
                    :key="i"
                    class="pa-0"
                    :href="`/client/shop/${client.id}/`"
                  >
                    <v-list-item-icon>
                      <v-img :src="client.assesment_price.client_shop.img" width="100" height="auto" :class="`rounded-lg`"></v-img>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>{{client.assesment_price.client_shop.name}}</v-list-item-title>
                    </v-list-item-content>
                    <!-- <v-list-item-content class="assesment">
                      <div class="font-weight-bold">{{client.assesment_price.client_shop.like_count}}</div>
                    </v-list-item-content> -->
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
    name: 'ListAssesmentShop',
    data() {
      return {
        clients: [],
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
        url: '/client/',
      })
      .then(response => this.clients = response.data.results)
      .catch(error => console.log(error)); 
    },
  }
</script>

<style scoped>
  .assesment {
    position: absolute;
    right: 10px;
    bottom: 27px;
  }
</style>