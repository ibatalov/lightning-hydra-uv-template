from torchvision import transforms


img_augmentation_transformations = [
    transforms.RandomAffine((-15, 15), translate=(0.2, 0.2)),
    transforms.RandomHorizontalFlip(p=0.65),
    transforms.RandomRotation((-15, 15)),
    transforms.ColorJitter(hue=.05, saturation=.05),
]

train_preprocess = transforms.Compose([
    transforms.Resize((256, 256)),  # the correct size for eff net b1 is 224x224 but we random crop it later
    transforms.RandomCrop(224),
    transforms.ToTensor(),
    transforms.RandomApply(img_augmentation_transformations, 0.8),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

test_preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])


cifar10_train_preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(p=0.5),
    # transforms.RandomRotation((-15, 15)),
])
