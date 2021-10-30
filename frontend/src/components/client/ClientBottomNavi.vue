<template>
  <v-bottom-navigation
    :value="value"
    color="pink darken-1"
    fixed
  >
    <v-btn to="/client/shop/">
      <span>トップ</span>
      <v-icon>mdi-history</v-icon>
    </v-btn>

    <v-btn to="/client/auction/">
      <span>査定一覧</span>
      <v-icon>mdi-format-list-bulleted</v-icon>
    </v-btn>
    
    <v-btn to="/client/visit-reservation/">
      <span>来店予約</span>
      <v-icon>mdi-heart-outline</v-icon>
    </v-btn>

    <v-btn to="/client/pr/">
      <span>店舗PR</span>
      <v-icon>mdi-pencil-outline</v-icon>
    </v-btn>

    <v-btn to="/client/contact/">
      <span>問い合わせ</span>
      <v-icon>mdi-chat-processing-outline</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
  export default {
    data(){
      return {
        dialog: false,
      }
    }
  }
</script>