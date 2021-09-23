<template>
  <div>
    <div>
      <h2>Confirmation</h2>
      <p>Name: {{ form.first_name }} {{ form.last_name }}</p>
      <p>Email: {{ form.email }}</p>
      <p>Tel: {{ form.tel }}</p>
      <p>Birthday: {{ form.birthday }}</p>
		</div>
  </div>
</template>

<script>
  export default {
    props: {
      form: Object
    }
  }
</script>
