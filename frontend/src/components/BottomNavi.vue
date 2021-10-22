<template>
  <v-bottom-navigation
    :value="value"
    color="dark"
    fixed
  >
    <v-btn>
      <span>探す</span>

      <v-icon>mdi-history</v-icon>
    </v-btn>

    <v-btn>
      <span>お気に入り</span>

      <v-icon>mdi-heart</v-icon>
    </v-btn>

    <v-btn>
      <span>マップ</span>

      <v-icon>mdi-map-marker</v-icon>
    </v-btn>

    <v-btn>
      <span>受信トレイ</span>

      <v-icon>mdi-email-outline</v-icon>
    </v-btn>

    <v-btn>
      <span>マイページ</span>

      <v-icon>mdi-account</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
  export default {
    data(){
      return {
        value: 1 
      }
    }
  }
</script>