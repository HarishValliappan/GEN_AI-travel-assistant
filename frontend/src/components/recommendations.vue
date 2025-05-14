<template>
  <div>
    <h1>Recommendations</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>
      <ul>
        <li v-for="recommendation in recommendations" :key="recommendation.id">
          {{ recommendation.name }} - {{ recommendation.description }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      recommendations: [],
      loading: false,
      error: null,
    };
  },
  mounted() {
    this.fetchRecommendations();
  },
  methods: {
    async fetchRecommendations() {
      this.loading = true;
      try {
        const response = await api.getRecommendations({ city: 'ExampleCity' }); // Example parameter
        this.recommendations = response.data;
      } catch (error) {
        this.error = error.message || 'Failed to fetch recommendations';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
