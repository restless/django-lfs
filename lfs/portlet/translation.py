try:
    from modeltranslation.translator import translator, TranslationOptions
    from .models import TextPortlet, AverageRatingPortlet, CartPortlet, CategoriesPortlet, DeliveryTimePortlet,\
        FeaturedPortlet, FilterPortlet, ForsalePortlet, LatestPortlet, PagesPortlet, RecentProductsPortlet,\
        RelatedProductsPortlet, TopsellerPortlet


    # AverageRatingPortlet
    class AverageRatingPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(AverageRatingPortlet, AverageRatingPortletTranslationOptions)

    # CartPortlet
    class CartPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(CartPortlet, CartPortletTranslationOptions)

    # CategoriesPortlet
    class CategoriesPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(CategoriesPortlet, CategoriesPortletTranslationOptions)

    # DeliveryTimePortlet
    class DeliveryTimePortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(DeliveryTimePortlet, DeliveryTimePortletTranslationOptions)

    # FeaturedPortlet
    class FeaturedPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(FeaturedPortlet, FeaturedPortletTranslationOptions)

    # FilterPortlet
    class FilterPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(FilterPortlet, FilterPortletTranslationOptions)

    # ForsalePortlet
    class ForsalePortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(ForsalePortlet, ForsalePortletTranslationOptions)

    # LatestPortlet
    class LatestPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(LatestPortlet, LatestPortletTranslationOptions)

    # PagesPortlet
    class PagesPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(PagesPortlet, PagesPortletTranslationOptions)

    # RecentProductsPortlet
    class RecentProductsPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(RecentProductsPortlet, RecentProductsPortletTranslationOptions)

    # RelatedProductsPortlet
    class RelatedProductsPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(RelatedProductsPortlet, RelatedProductsPortletTranslationOptions)

    # TextPortlet
    class TextPortletTranslationOptions(TranslationOptions):
        fields = ('title', 'text', )
    translator.register(TextPortlet, TextPortletTranslationOptions)

    # TopsellerPortlet
    class TopsellerPortletTranslationOptions(TranslationOptions):
        fields = ('title', )
    translator.register(TopsellerPortlet, TopsellerPortletTranslationOptions)

except ImportError:
    pass
