<template>
    <li class='mtab'>
        <slot></slot>
    </li>
</template>
<script>
export default {}
</script>
<style>
.mtab {
    float: left;
}

.active {
    border: 1px solid #ddd;
}
</style>
