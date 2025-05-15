<template>
  <section class="min-h-screen w-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 text-white py-10">
    <div class="container mx-auto flex flex-col md:flex-row h-full">
      <!-- Image Section -->
      <div class="w-full md:w-1/2 p-4 flex items-center justify-center h-full">
        <img
          :src="images[currentImageIndex]"
          alt="Travel"
          class="rounded-2xl shadow-2xl w-full h-full object-cover transition duration-700 ease-in-out transform hover:scale-105 hover:shadow-purple-500"
        />
      </div>

      <!-- Form Section -->
      <div class="w-full md:w-1/2 p-8">
        <!-- Vue.js Logo -->
        <div class="flex justify-center mb-4">
          <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" alt="Vue Logo" class="h-12" />
        </div>

        <h2 class="text-4xl font-bold text-center text-purple-400 mb-10">
          Plan Your Trip with <span class="text-white">WayfarerAI</span>
        </h2>

        <div class="space-y-5">
          <div>
            <label for="from_city" class="block text-gray-300 text-sm font-semibold mb-1">From City:</label>
            <input
              type="text"
              id="from_city"
              v-model="from_city"
              class="w-full py-2 px-4 rounded bg-gray-100 text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
              placeholder="Enter your origin city"
            />
          </div>

          <div>
            <label for="destination_city" class="block text-gray-300 text-sm font-semibold mb-1">Destination:</label>
            <input
              type="text"
              id="destination_city"
              v-model="destination_city"
              class="w-full py-2 px-4 rounded bg-gray-100 text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
              placeholder="Enter your destination"
            />
          </div>
          
          <div>
            <label for="start_date" class="block text-gray-300 text-sm font-semibold mb-1">Start Date:</label>
            <input
              type="date"
              id="start_date"
              v-model="start_date"
              class="w-full py-2 px-4 rounded bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
          </div>

          <div>
            <label for="end_date" class="block text-gray-300 text-sm font-semibold mb-1">End Date:</label>
            <input
              type="date"
              id="end_date"
              v-model="end_date"
              class="w-full py-2 px-4 rounded bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
          </div>

          <div>
            <label for="interests" class="block text-gray-300 text-sm font-semibold mb-1">Interests:</label>
            <textarea
              id="interests"
              v-model="interests"
              rows="3"
              class="w-full py-2 px-4 rounded bg-gray-100 text-gray-800 focus:outline-none focus:ring-2 focus:ring-purple-500"
              placeholder="e.g., sightseeing, food, adventure"
            ></textarea>
          </div>

          <div class="flex justify-center pt-2">
            <button
              class="group relative inline-flex items-center justify-center p-2 px-4 py-2 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-white rounded-full shadow-md transform hover:scale-105 hover:shadow-purple-500 text-sm"
              @click="getRecommendations"
            >
              <span class="absolute inset-0 flex items-center justify-center w-full h-full bg-gray-900"></span>
              <span class="relative text-white group-hover:text-white">Generate Recommendations</span>
            </button>
          </div>
          
          <div v-if="loading" class="text-center text-gray-300">
            Preparing, please wait...
          </div>
          <div class="flex justify-center pt-2" v-if="recommendations.length > 0 && !loading" >
            <button
              class="group relative inline-flex items-center justify-center p-2 px-4 py-2 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-white rounded-full shadow-md transform hover:scale-105 hover:shadow-purple-500 text-sm"
              @click="downloadPdf"
            >
              <span class="absolute inset-0 flex items-center justify-center w-full h-full bg-gray-900"></span>
              <span class="absolute right-0 w-10 h-10 duration-200 transform translate-x-full group-hover:translate-x-0 ease">
                <svg class="h-6 w-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </span>
              <span class="relative text-white group-hover:text-white">Download PDF</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import travelImage1 from '../assets/img1.avif';
import travelImage2 from '../assets/img2.jpg';
import travelImage3 from '../assets/img3.png';
import Recommendations from './recommendations.vue';
import { generatePdf } from '../services/pdfDesign';

export default {
  components: {
    Recommendations
  },
  data() {
    return {
      from_city: '',
      destination_city: '',
      interests: '',
      start_date: new Date().toISOString().split('T')[0],
      end_date: new Date().toISOString().split('T')[0],
      images: [travelImage1, travelImage2, travelImage3],
      currentImageIndex: 0,
      recommendations: [],
      loading: false,
    };
  },
  watch: {
    loading(newLoading) {
      if (newLoading) {
        // You can add animation logic here if needed
        console.log("Loading started...");
      } else {
        console.log("Loading finished.");
      }
    }
  },
  mounted() {
    setInterval(() => {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
    }, 3000);
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return date.toLocaleDateString(undefined, options);
    },
    async getRecommendations() {
      this.loading = true;
      try {
        const response = await fetch('http://localhost:5000/api/recommendations', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            from_city: this.from_city,
            destination_city: this.destination_city,
            start_date: this.formatDate(this.start_date),
            end_date: this.formatDate(this.end_date),
            interests: this.interests,
          }),
        });

        const data = await response.json();
        this.recommendations = data.recommendations;
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      } finally {
        this.loading = false;
      }
    },
    downloadPdf() {
      generatePdf(this.recommendations);
    },
  },
};
</script>

<style scoped>
input::placeholder,
textarea::placeholder {
  color: #a0aec0;
}
</style>
