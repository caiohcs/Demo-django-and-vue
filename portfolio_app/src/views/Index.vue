<template>
    <div>
        <h1 class="title">This is a Django/Vue demo app</h1>
            <ul>
                <li v-for="technology in technologies" v-bind:key="technology">
                    <Technology v-bind:technology="technology" />
                </li>

            </ul>
    </div>
</template>

<script>
import axios from 'axios';
import Technology from '../components/Technology'

export default {
    name: 'Index',
    components: {
        Technology
    },
    data() {
        return {
            technologies: [],
        }
    },
    methods: {
        
    },
    mounted() {
            axios.get('http://127.0.0.1:9000/api/portfolio/')
            .then( response => {
                this.technologies = response.data;
                console.log(this.portfolio);
            }).catch(err => { console.log(err); });
    }
}
</script>

<style scoped>
    .title {
        color: #f6f6f6;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
    }
</style>