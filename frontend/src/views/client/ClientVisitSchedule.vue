<template>
  <div>
    <v-app>
      <ClientHeader />
      <ClientGlobalMenu />
      <v-container>
        <h2>来店スケジュール </h2>
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
      </v-container>
    </v-app>
  </div>
</template>

<script>
  import ClientHeader from '@/components/client/ClientHeader.vue'
  import ClientGlobalMenu from '@/components/client/ClientGlobalMenu.vue'
  import api from '@/services/api'
  import moment from 'moment';
  
  export default {
    data(){
      return {
        events: [],
        value: moment().format('yyyy-MM-DD'),
        focus: '',
        type: 'month',
        selectedEvent: {},
        selectedElement: null,
        selectedOpen: false,
      }
    },
    components: {
      ClientHeader,
      ClientGlobalMenu,
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
    mounted() {
      api({
        method: 'get',
        url: '/api/v1/api/visit_reservation/',
      })
      .then(response => this.events = response.data.results)
      .catch(error => console.log(error));
    }
  }
</script>