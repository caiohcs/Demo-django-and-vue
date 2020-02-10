<template>
    <div class="body">
        <div class="name">{{technology.name}}</div> <div class="description">{{technology.description}}</div> 
    </div>
</template>

<script>
export default {
    name: 'Technology',
    props: ['technology']
}
</script>

<style scoped>
    .body {
        background: #7e7e7e;
        padding: 10px;
        border-bottom: 1px #ccc dotted;
    }

    .is-complete {
        text-decoration: line-through;
    }

    .del {
        background: #ff0000;
        color: #fff;
        border: none;
        padding: 5px 9px;
        border-radius: 50%;
        cursor: pointer;
        float: right;
    }

    .name {
        float: left;
        font-size: 20px;
        color: #ffffff;
    }

    .description {
        font-size: 18px;
        color: #ffffff;
    }
</style>