<template>
  <div>
      <div>
        <h2>Confirmation</h2>
        これ{{form}}
      <p>Name: {{ form.firstName }} {{ form.lastName }}</p>
      <p>Email: {{ form.Email }}</p>
      <p>Tel: {{ form.tel }}</p>
      <p>Birthday: {{ form.birthday }}</p>
		</div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    props: {
      form: Object
    }
  })
</script>
