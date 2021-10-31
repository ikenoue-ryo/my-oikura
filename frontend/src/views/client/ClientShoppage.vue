<template>
  <div>
    <v-img 
      :src="shop_infos.img" 
      width="100%" 
      class="mx-auto ma-0"
    >
      <v-icon @click="$router.back()" class="pa-4" size="30">mdi-arrow-left</v-icon>
    </v-img>

    <v-container class="pa-8">
      <v-row>
        <v-col>
          <h2>{{ shop_infos.name }}</h2>
        </v-col>
      </v-row>
      <v-row
        align="center"
        class="mt-3 ml-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>
        <div class="grey--text ms-4">
          4.5 (413)
        </div>
      </v-row>
      <v-row>
        <v-col>{{ shop_infos.place }}</v-col>
      </v-row>
      <v-row class="mb-3">
        <v-col>{{ shop_infos.tel }}</v-col>
      </v-row>
      
      <v-row>
        <v-col>
          <h3>店舗マップ</h3>
          <v-img
          class="white--text align-end google-map rounded-xl"
          src="@/assets/googlemap.jpeg"
          >
          </v-img>
        </v-col>
      </v-row>

      <v-divider></v-divider>

      <v-row>
        <v-col>
          <h3>店舗紹介</h3>
          <div v-for="shop in shop_Pr" :key="shop.id">
            <p><v-img :src="shop.img" width="500px"></v-img></p>
            <p>{{shop.text}}</p>
            <!-- <p>{{shop.created_at}}</p> -->
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <h3>来店スケジュール</h3>
          <v-sheet tile height="6vh" color="grey lighten-3" class="d-flex align-center">
            <v-btn outlined small class="ma-4" @click="setToday">
              今日
            </v-btn>
            <v-btn icon @click="$refs.calendar.prev()">
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
            <v-btn icon @click="$refs.calendar.next()">
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
            <v-toolbar-title>{{ title }}</v-toolbar-title>
          </v-sheet>
          <v-sheet height="60vh">
            <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
            @click:more="viewDay"
            @click:date="viewDay"
            @change="updateRange"
          ></v-calendar>
            <v-menu
              v-model="selectedOpen"
              :close-on-content-click="false"
              :activator="selectedElement"
              offset-x
            >
              <v-card
                color="grey lighten-4"
                min-width="350px"
                flat
              >
                <v-toolbar
                  dark
                >
                  <v-toolbar-title v-html="selectedEvent.name + '様'"></v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-btn icon>
                    <v-icon>mdi-heart</v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon>mdi-dots-vertical</v-icon>
                  </v-btn>
                </v-toolbar>
                <v-card-text>
                  来店日時：<span v-html="selectedEvent.start"></span><br>
                  来店者名：<span v-html="selectedEvent.name"></span> 様<br>
                  電話番号：<span v-html="selectedEvent.tel"></span><br>
                  Email：<span v-html="selectedEvent.email"></span><br>
                  Comment：<span v-html="selectedEvent.comment"></span>
                </v-card-text>
                <v-card-actions>
                  <v-btn
                    text
                    color="secondary"
                    @click="selectedOpen = false"
                  >
                    閉じる
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-menu>
          </v-sheet>
        </v-col>
      </v-row>
      <v-divider></v-divider>
    
      <v-row>
        <v-col>
          <h3>レビュー ({{shop_Review.length}}件)</h3>
          <template>
            <v-item-group class="d-flex overflow-x-auto">
              <v-container v-for="review in shop_Review" :key="review" class="pa-0">
                <v-scroll-y-transition>
                  <v-card
                    width="190"
                    height="100%"
                    class="ml-0 mr-3"
                  >
                    <v-card-text>
                      <v-list-item class="grow">
                        <v-list-item-avatar color="grey darken-3">
                          <v-img
                            class="elevation-6"
                            :src="review.profile.img"
                          ></v-img>
                        </v-list-item-avatar>

                        <v-list-item-content>
                          <v-list-item-title>{{review.profile.nickname}}</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-rating
                        v-model="review.score"
                        background-color="orange lighten-3"
                        color="orange"
                        size="20"
                        dense
                        readonly
                        pa-0
                      >
                      </v-rating>
                      <div class="text--primary">
                        {{review.comment}}
                      </div>
                      <p>{{review.created_at}}</p>
                    </v-card-text>

                    <v-expand-transition>
                      <v-card
                        v-if="reveal"
                        class="transition-fast-in-fast-out v-card--reveal"
                        style="height: 100%;"
                      >
                        <v-card-text class="pb-0">
                          <p class="text-h4 text--primary">
                            Origin
                          </p>
                          <p>late 16th century (as a noun denoting a place where alms were distributed): from medieval Latin eleemosynarius, from late Latin eleemosyna ‘alms’, from Greek eleēmosunē ‘compassion’ </p>
                        </v-card-text>
                        <v-card-actions class="pt-0">
                          <v-btn
                            text
                            color="teal accent-4"
                            @click="reveal = false"
                          >
                            Close
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-expand-transition>
                  </v-card>
                </v-scroll-y-transition>
              </v-container>
            </v-item-group>
          </template>
          <v-row justify="center" class="py-5 px-3">
            <v-dialog
              v-model="dialog"
              fullscreen
              hide-overlay
              transition="dialog-bottom-transition"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  type="submit"
                  color="pink darken-1"
                  x-large
                  block
                  outlined
                  class="white--text font-weight-bold body-1"
                  v-bind="attrs"
                  v-on="on"
                >
                  {{shop_Review.length}}件のレビューをすべて表示
                </v-btn>
              </template>
              <v-card>
                <v-toolbar
                  dark
                  color="primary"
                >
                  <v-btn
                    icon
                    dark
                    @click="dialog = false"
                  >
                    <v-icon>mdi-arrow-left</v-icon>
                  </v-btn>
                  <v-toolbar-title>{{shop_Review.length}}件のレビュー</v-toolbar-title>
                </v-toolbar>
                <v-list
                  three-line
                  subheader
                >
                  <v-subheader>Review</v-subheader>
                  <v-container v-for="review in shop_Review" :key="review" class="pa-0">
                    <v-list-item>
                      <v-list-item-action>
                        <v-list-item-avatar color="grey darken-3">
                          <v-img
                            class="elevation-6"
                            :src="review.profile.img"
                          ></v-img>
                        </v-list-item-avatar>
                      </v-list-item-action>
                      <v-list-item-content>
                        <v-list-item-title>
                          {{review.profile.nickname}}
                        </v-list-item-title>
                        <v-rating
                            v-model="review.score"
                            background-color="orange lighten-3"
                            color="orange"
                            size="15"
                            dense
                            readonly
                            pa-0
                          >
                          </v-rating>
                        <v-list-item-subtitle>{{review.comment}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-container>
                </v-list>
              </v-card>
            </v-dialog>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <div class="push"></div>
    <BottomNavi />
  </div>
</template>

<script>
  import BottomNavi from '@/components/BottomNavi.vue'
  // import VisitReservation from '@/components/VisitReservation.vue'
  import api from '@/services/api'
  import moment from 'moment';

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

        events: [],
        value: moment().format('yyyy-MM-DD'),
        focus: '',
        type: 'month',
        selectedEvent: {},
        selectedElement: null,
        selectedOpen: false,

        // dialog
        dialog: false,
        notifications: false,
        sound: true,
        widgets: false,
      }
    },
    components: {
      BottomNavi,
      // VisitReservation,
    },
    methods: {
      setToday() {
        this.value = moment().format('yyyy-MM-DD');
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          requestAnimationFrame(() => requestAnimationFrame(() => open()))
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      },
      viewDay({ date }) {
        alert(`date: ${date}`);
      },
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

      api({
        method: 'get',
        url: '/api/v1/api/visit_reservation/',
      })
      .then(response => this.events = response.data.results.filter(reservation => reservation.email === this.email))
      .catch(error => console.log(error));
    },
    computed: {
      email() {
        return this.$store.getters['auth/email']
      },
      username() {
        return this.$store.getters['auth/username']
      },
      shop_infos() {
        const shop_info = this.shop_Info;
        return shop_info;
      }
    }
  }
</script>

<style>
  .push {
    height: 55px;/*フッターと同じ高さに指定*/
  }
</style>