<template>
  <div class="hello">
    wesh la fratterie
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      users: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  created () {
    axios.get('http://172.28.0.2:5000/users')
      .then(response => {
        // JSON responses are automatically parsed.
        this.users = response.data
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e)
      })
  }
}
</script>
<style scoped>

</style>
