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

    <v-btn
      @click="dialog = !dialog">
      <span>査定</span>

      <v-icon>mdi-camera-wireless-outline</v-icon>
    </v-btn>
    <v-dialog
      v-model="dialog"
      max-width="500px"
    >
      <v-card>
        <v-card-text>
          <v-text-field label="File name"></v-text-field>

          <small class="grey--text">* This doesn't actually save.</small>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            text
            color="primary"
            @click="dialog = false"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-btn>
      <span>受信トレイ</span>

      <v-icon>mdi-email-outline</v-icon>
    </v-btn>

    <v-btn href="/mypage">
      <span>マイページ</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
  export default {
    data(){
      return {
        value: 1,

        dialog: false,
      }
    }
  }
</script>