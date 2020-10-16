from django.shortcuts import render
from django.views import generic
from . models import Person, Planet, Species, Vehicles


class HomePageView(generic.TemplateView):
	template_name = 'webapp/home.html'


class AboutPageView(generic.TemplateView):
	template_name = 'webapp/about.html'


# def about(request):
#     # stripe_key = settings.STRIPE_KEYS['publishable']
#     # data = cache.get('resource_data')
#     # if not data:
#     #     data = get_resource_stats()
#     #     cache.set('resource_data', data, 10000)
#     # data['stripe_key'] = stripe_key

#     data = 'A long time ago in a galaxy far, far away.'
#     return render(request, "about.html", data)


class DocsPageView(generic.TemplateView):
	template_name = 'webapp/docs.html'


class PersonListView(generic.ListView):
	model = Person
	context_object_name = 'persons'
	template_name = 'webapp/people.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Person.objects.all()
		# return Person.objects.select_related('homeworld').order_by('name')


class PlanetListView(generic.ListView):
	model = Planet
	context_object_name = 'planets'
	template_name = 'webapp/planets.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Planet.objects.all()
		# return Person.objects.select_related('homeworld').order_by('name')


class SpeciesListView(generic.ListView):
	model = Species
	context_object_name = 'species'
	template_name = 'webapp/species.html'
	# paginate_by = 20

	# def dispatch(self, *args, **kwargs):
	# 	return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Species.objects.all()
		# return Species.objects.select_related('homeworld').order_by('name')

class VehiclesListView(generic.ListView):
	model = Vehicles
	context_object_name = 'vehicles'
	template_name = 'webapp/vehicles.html'

	def get_queryset(self):
		return Vehicles.objects.all()
