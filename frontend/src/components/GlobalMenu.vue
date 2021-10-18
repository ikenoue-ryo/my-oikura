<template>
  <div>
    <v-app-bar flat>
      <v-toolbar-items>
        <v-btn text :to="`/`" width="150">トップ</v-btn>
        <v-btn text :to="`/offer-form/`" width="150">査定依頼</v-btn>
        <v-btn text :to="`/client-shop-search`" width="150">店舗を探す</v-btn>
        <v-btn text :to="`/car-search`" width="150">相場を見る</v-btn>
        <v-btn text width="150">おいくらマガジン</v-btn>
        <v-btn text width="150">掲載のお知らせ</v-btn>
      </v-toolbar-items>
    </v-app-bar>
  </div>
</template>

<style>
</style>