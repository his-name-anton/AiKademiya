<template>
  <fwb-navbar>
    <template #logo>
      <fwb-navbar-logo alt="AiKademiya Logo" image-url="/static/images/logo.svg" link="/">
        AiKademiya
      </fwb-navbar-logo>
    </template>

    <template #default="{ isShowMenu }">
      <fwb-navbar-collapse :is-show-menu="isShowMenu">
        <fwb-navbar-link link="/">Главная</fwb-navbar-link>
        <fwb-navbar-link link="/about">О нас</fwb-navbar-link>
        <fwb-navbar-link link="/pricing">Тарифы</fwb-navbar-link>
        <fwb-navbar-link link="/contacts">Контакты</fwb-navbar-link>
      </fwb-navbar-collapse>
    </template>

    <template #right-side>
      <fwb-button tag="a" href="/login">
        Войти
      </fwb-button>
    </template>
  </fwb-navbar>
</template>

<script setup>
import {
  FwbButton,
  FwbNavbar,
  FwbNavbarCollapse,
  FwbNavbarLink,
  FwbNavbarLogo,
} from 'flowbite-vue'
</script>