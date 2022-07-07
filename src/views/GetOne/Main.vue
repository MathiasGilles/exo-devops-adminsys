<template>
  <div>
    Formulaire update analyse avec l'id actuellement: {{ id }}
    {{ formData.description }}
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
      <button>Delete</button>
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
    UpdateAnalyse: function () {
      API
          .put('api001', '/updateAnalyse', this.formData)
          .then(response => {
            console.log(response)
            return response;
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
}
</script>

<style scoped>

</style>