<template>
  <div>
    <h2>Form modification id: {{id}}</h2>
    <br>
    <label for="title">Titre</label>
    <br>
    <input type="text" name="title" v-model="formData.title"/>
    <br>
    <label for="description">Description</label>
    <br>
    <input type="text" name="description" id="description" v-model="formData.description">
    <br>
    <div style="display: flex">
      <button @click="deleteAnalyse">Delete</button>
      <button @click="UpdateAnalyse">Save</button>
    </div>
    <br>
    <input type="file"/>
    <br>
    <input type="text">
    <br>
    <br>
  </div>
</template>

<script>
import {API} from "aws-amplify";

export default {
  name: "GetOne",
  mounted() {
    this.getId()
  },
  data: function () {
    return {
      id: this.$route.params.id,
      formData: {
        title: "oui",
        description: "Description"
      }
    }
  },
  methods: {
    UpdateAnalyse: async function () {
      const option = {
        body: {
          id: this.id,
          ...this.formData
        }
      }
      console.log(option)
      const response = await API.post('api001', '/updateAnalyse', option)
      console.log(response);
    },
    deleteAnalyse: async function () {
      const option = {
        body: {
          id: this.id
        }
      }
      const response = await API.post('api001', '/deleteAnalyse', option).then(
          () => this.$router.push('/')
      );
      console.log(response)
    }
  }
}
</script>

<style scoped>

</style>