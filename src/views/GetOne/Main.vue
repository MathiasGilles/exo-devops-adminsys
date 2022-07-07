<template>
  <div v-if="formData">
    <h2>Form modification id: {{id}}</h2>
    <br>
    <label for="title">Titre</label>
    <br>
    <input type="text" name="title" v-model=" formData.title"/>
    <br>
    <label for="description">Description</label>
    <br>
    <input type="text" name="description" id="description" v-model="formData.description">
    <br>
    <div style="display: flex">
      <button>Delete</button>
      <button @click="UpdateAnalyse">Save</button>
    </div>
    <br>
    <input type="file"/>
    <br>
    <input type="text">
    <br>
    <br>
    <img style="width: 200px" :src="storedImage" alt="">
  </div>
</template>

<script>
import {API, Storage} from "aws-amplify";

export default {
  name: "GetOne",
  mounted() {
    this.getStorage()
  },
  data: function () {
    return {
      id: this.$route.params.id,
      storedImage: "",
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
    async getStorage(){
      return this.storedImage = await Storage.get('img.jpeg')
    }
  }
}
</script>

<style scoped>

</style>