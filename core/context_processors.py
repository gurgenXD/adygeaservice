# from feedback.forms import CallBackForm
# from core.models import Index, TitleTag
# from contacts.models import Social


def context_info(request):
    # callback_form = CallBackForm()
    # socials = Social.objects.all()
    #
    # index = Index.objects.first()
    #
    # main_phone = index.phone
    # main_address = index.address
    #
    # seo_titles = TitleTag.objects.all()

    context = {
        # 'callback_form': callback_form,
        # 'socials': socials,
        # 'main_phone': main_phone,
        # 'main_address': main_address,
        # 'seo_titles': seo_titles,
    }

    return context