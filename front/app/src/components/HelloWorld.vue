<template>
  <div class="hello">
    <table id="customers">
      <tr>
        <th>Id</th>
        <th>Full name</th>
        <th>Email</th>
      </tr>
      <tr v-for="user in users" :key="user[0]">
        <td>{{user[0]}}</td>
        <td>{{user[1]}}</td>
        <td>{{user[2]}}</td>
      </tr>
    </table>
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
    axios.get('http://localhost:5000//api/users')
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
  .hello{
    margin: 0 20%;
  }
  #customers {
    font-family: Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
  }

  #customers td, #customers th {
    border: 1px solid #ddd;
    padding: 8px;
  }

  #customers tr:nth-child(even){background-color: #f2f2f2;}

  #customers tr:hover {background-color: #ddd;}

  #customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #04AA6D;
    color: white;
  }
</style>
