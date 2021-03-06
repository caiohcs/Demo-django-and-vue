import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    redirect: '/index'
  },
  {
    path: "/create",
    name: "create",
    component: () => import("../views/Create.vue")
  },
  {
    path: "/edit/:id",
    name: "edit",
    component: () => import("../views/Edit.vue")
  },
  {
    path: "/index",
    name: "index",
    component: () => import("../views/Index.vue")
  },
]

const router = new VueRouter({
  routes
})

export default router
