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

          <!-- Normal Single-Date Calendar -->
          <div>
            <label for="travel_date" class="block text-gray-300 text-sm font-semibold mb-1">Travel Date:</label>
            <input
              type="date"
              id="travel_date"
              v-model="travel_date"
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

          <div class="flex justify-center pt-4">
            <button
              class="group relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden font-medium text-indigo-600 transition duration-300 ease-out border-2 border-white rounded-full shadow-md transform hover:scale-105 hover:shadow-purple-500"
              @click="getRecommendations"
            >
              <span class="absolute inset-0 flex items-center justify-center w-full h-full bg-gray-900"></span>
              <span class="absolute right-0 w-10 h-10 duration-200 transform translate-x-full group-hover:translate-x-0 ease">
                <svg class="h-6 w-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </span>
              <span class="relative text-white group-hover:text-white">Get Recommendations</span>
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

export default {
  data() {
    return {
      from_city: '',
      destination_city: '',
      interests: '',
      travel_date: new Date().toISOString().split('T')[0], // Default to today
      images: [travelImage1, travelImage2, travelImage3],
      currentImageIndex: 0,
    };
  },
  mounted() {
    setInterval(() => {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
    }, 3000);
  },
  methods: {
    getRecommendations() {
      console.log('From City:', this.from_city);
      console.log('Destination:', this.destination_city);
      console.log('Travel Date:', this.travel_date);
      console.log('Interests:', this.interests);
      // API call logic goes here
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
