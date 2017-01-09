<template>
	<div>
		<ul>
			<li v-for="qcase in this.$store.state.qcases">
				<p>{{ qcase.issue[0].content.desc }}</p>
				<p>Token: {{ qcase.token }}</p>
				<p>SN: {{ qcase.initArg.SN }}</p>
				<p>Email: {{ qcase.email }}</p>
				<p>Phone: {{ qcase.phone }}</p>
				<p>Birthday : {{ qcase.birthday  }}</p>
				<p>Country : {{ qcase.country  }}</p>
				<p>RequestDate : <span>{{getValue(qcase.issue[0].reporttime)}}<span></p>
			</li>
		</ul>
	</div>	
</template>
<script>
export default {
	methods: {
		getValue: function(value){				
			return "value form methods" + value
		}
	}
}
</script>
